document.addEventListener("DOMContentLoaded", function() {
    const borrowButtons = document.querySelectorAll(".borrow-btn");

    borrowButtons.forEach(button => {
        button.addEventListener("click", function() {
            const bookId = this.getAttribute("data-bookid");

            fetch('/borrow', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ book_id: bookId })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                location.reload(); // Refresh page to update book availability
            });
        });
    });
});
