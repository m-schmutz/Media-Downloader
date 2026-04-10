// Get DOM elements
const form = document.getElementById("download-form");
const container = document.getElementById("file-info-container");
const submitBtn = form.querySelector(".submit-btn");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    container.innerHTML = ""; // clear previous results

    const url = document.getElementById("url").value;
    const type = document.getElementById("type").value;

    // --- NEW: Show loading state ---
    submitBtn.disabled = true;
    submitBtn.textContent = "Checking...";
    container.innerHTML = `<div class="loading">Checking link, please wait...</div>`;

    try {
        const response = await fetch("/api/check-link", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ url, type })
        });

        const data = await response.json();

        
        // Clear loading message
        container.innerHTML = "";

        if (!response.ok) {
            const errorBox = document.createElement("div");
            errorBox.classList.add("error-box");
            errorBox.innerHTML = `
                <h2>Error</h2>
                <p>${data.error || "An unknown error occurred."}</p>
            `;
            container.appendChild(errorBox);
            return;
        }

        // Extract file info
        const info = data["file-info"];

        const infoBox = document.createElement("div");
        infoBox.classList.add("file-info-box");

        infoBox.innerHTML = `
            <h2>File Information</h2>
            <img src="${info.thumbnail}" alt="Thumbnail" class="thumbnail">
            
            <p><strong>Type:</strong> ${info.type}</p>
            <p><strong>Uploader:</strong> ${info.uploader}</p>
            <p><strong>Title:</strong> ${info.title}</p>
            <p><strong>Duration:</strong> ${info.duration_string}</p>
            <p><strong>Resolution:</strong> ${info.resolution}</p>
            <p><strong>Filesize:</strong> ${info.filesize_approx}</p>
            <p><strong>Video Codec:</strong> ${info.vcodec}</p>
            <p><strong>Audio Codec:</strong> ${info.acodec}</p>
        `;

        container.appendChild(infoBox);

    } catch (err) {
        container.innerHTML = `
            <div class="error-box">
                <h2>Error</h2>
                <p>Failed to connect to server.</p>
            </div>
        `;
        console.error(err);
    }

    // --- NEW: Reset button state ---
    submitBtn.disabled = false;
    submitBtn.textContent = "Check Availability";
});
