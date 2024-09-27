function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

    function getCurrentUserId() {
        return fetch('/auth/current_user/')
            .then(response => {
                if (response.ok) {
                    return response.json();
                }
                throw new Error('User not logged in');
            })
            .then(data => {
                return data.userId; // Adjust based on your API response
            })
            .catch(error => {
                console.error('Error fetching user ID:', error);
                return null; // Handle as necessary
            });
    }

