document.addEventListener('DOMContentLoaded', function() {
    const calendarContainer = document.getElementById('content-calendar-container');
    const userPreferences = JSON.parse(localStorage.getItem('userPreferences')) || {};

    // Initialize the calendar view
    function initializeCalendar() {
        // Placeholder for calendar initialization logic
        // This should integrate with a calendar library like FullCalendar
        // For example:
        // $('#calendar').fullCalendar({
        //     // Calendar options here
        // });
    }

    // Fetch content data and populate the calendar
    function fetchAndDisplayContent() {
        fetchContentData().then(contentItems => {
            contentItems.forEach(item => {
                // Add each content item to the calendar
                // For example:
                // $('#calendar').fullCalendar('renderEvent', {
                //     title: item.title,
                //     start: item.date,
                //     allDay: true
                // });
            });
        }).catch(error => {
            console.error('Error fetching content data:', error);
        });
    }

    // Schedule new content item
    function scheduleContentItem(contentItem) {
        scheduleContent(contentItem).then(response => {
            // Handle successful scheduling
            // For example, add the new item to the calendar view
            // $('#calendar').fullCalendar('renderEvent', {
            //     title: contentItem.title,
            //     start: contentItem.date,
            //     allDay: true
            // });
        }).catch(error => {
            console.error('Error scheduling content:', error);
        });
    }

    // Event listener for content item submission
    document.getElementById('content-schedule-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(event.target);
        const contentItem = {
            title: formData.get('title'),
            date: formData.get('date'),
            platform: formData.get('platform'),
            description: formData.get('description')
        };
        scheduleContentItem(contentItem);
    });

    // Load user preferences and initialize the calendar
    if (userPreferences.contentCalendar) {
        // Apply user preferences to the calendar
    }
    initializeCalendar();
    fetchAndDisplayContent();
});

// Shared function to fetch content data from the API
function fetchContentData() {
    return fetch('/api/content', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKeys.contentApi}`
        }
    }).then(response => response.json());
}

// Shared function to schedule content
function scheduleContent(contentItem) {
    return fetch('/api/content/schedule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKeys.contentApi}`
        },
        body: JSON.stringify(contentItem)
    }).then(response => response.json());
}