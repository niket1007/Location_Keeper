let manualTags = [];

// Get current location for link generation
function getCurrentLocationForLink() {
    const btn = document.getElementById('getLocationLinkBtn');
    const linkField = document.getElementById('locationLink');
    const originalText = btn.innerHTML;

    if (!navigator.geolocation) {
        showError('geolocation-unsupported=error');
        return;
    }

    btn.innerHTML = '📍 Getting...';
    btn.disabled = true;
    // hideMessages();

    const options = {
        enableHighAccuracy: true,
        timeout: 15000,
        maximumAge: 0
    };

    navigator.geolocation.getCurrentPosition(
        function(position) {
            const lat = position.coords.latitude;
            const lng = position.coords.longitude;
            
            // Generate Google Maps link
            const gmapLink = `https://www.google.com/maps?q=${lat},${lng}`;
            linkField.value = gmapLink;
            
            btn.innerHTML = '✅ Location Added';
            btn.disabled = false;
            
            // Reset button text after 3 seconds
            setTimeout(() => {
                btn.innerHTML = originalText;
            }, 3000);
        },
        function(error) {
            showError('geolocation-fetch=error');
        },
        options
    );
}

// Display tag when edit page
function showTags() {
    tags = document.getElementById('hiddenLocationTags').value;
    if(tags.length != 0) {
        manualTags = tags.split(",");
        updateTagsDisplay();
    }
}

// Handle tag input
function handleTagInput(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        const input = event.target;
        const tagValue = input.value.trim().toLowerCase();

        if (tagValue && tagValue.length > 0) {
            if (!manualTags.includes(tagValue)) {
                manualTags.push(tagValue);
                updateTagsDisplay();
            }
            input.value = '';
        }
    }
}

// Update tags display
function updateTagsDisplay() {
    const displayElement = document.getElementById('tagDisplay');
    const hiddenTags = document.getElementById('hiddenLocationTags');

    displayElement.innerHTML = '';
    manualTags.forEach((tag, index) => {
        const tagElement = document.createElement('div');
        tagElement.className = 'tag';
        tagElement.innerHTML = `
            ${tag} 
            <span class="tag-remove" onclick="removeTag(${index})">×</span>
        `;
        displayElement.appendChild(tagElement);
    });
    hiddenTags.value = manualTags.toString();
}

// Remove tag
function removeTag(index) {
    manualTags.splice(index, 1);
    updateTagsDisplay();
}

// Preview location on map
function previewOnMap() {
    const linkField = document.getElementById('locationLink');
    const link = linkField.value.trim();
    
    if (!link) {
        showError('geolocation-preview=error')
        return;
    }
    
    window.open(link, '_blank');
}

// Utility functions
function showError(query_param) {
    let url = window.location.href.split('?')[0]
    url = url + "?" + query_param
    window.location.href = url
}
