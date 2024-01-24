document.addEventListener('DOMContentLoaded', function() {
    const dashboardContainer = document.getElementById('dashboard-container');

    // Function to update the dashboard with the latest social media data
    function updateDashboard() {
        fetchSocialMediaData().then(data => {
            // Assuming fetchSocialMediaData returns an array of social media post objects
            data.forEach(post => {
                const postElement = createPostElement(post);
                dashboardContainer.appendChild(postElement);
            });
        }).catch(error => {
            console.error('Error fetching social media data:', error);
        });
    }

    // Function to create a DOM element for a social media post
    function createPostElement(post) {
        const postDiv = document.createElement('div');
        postDiv.className = 'post';

        const platformIcon = document.createElement('img');
        platformIcon.src = `images/${post.platform}_icon.png`; // Placeholder for platform-specific icons
        platformIcon.alt = `${post.platform} icon`;
        postDiv.appendChild(platformIcon);

        const postContent = document.createElement('p');
        postContent.textContent = post.content;
        postDiv.appendChild(postContent);

        const postAnalytics = document.createElement('span');
        postAnalytics.textContent = `Likes: ${post.likes}, Comments: ${post.comments}`;
        postDiv.appendChild(postAnalytics);

        return postDiv;
    }

    // Function to schedule a new post
    document.getElementById('schedule-post-btn').addEventListener('click', function() {
        const postDetails = {
            platform: document.getElementById('post-platform').value,
            content: document.getElementById('post-content').value,
            scheduleTime: document.getElementById('post-time').value
        };
        schedulePost(postDetails).then(response => {
            console.log('Post scheduled successfully:', response);
            updateDashboard();
        }).catch(error => {
            console.error('Error scheduling post:', error);
        });
    });

    // Initial dashboard update
    updateDashboard();

    // Set up periodic dashboard updates
    setInterval(updateDashboard, 60000); // Update every minute
});