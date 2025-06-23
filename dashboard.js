/*document.addEventListener("DOMContentLoaded", function() {
    // Fetch book data from backend
    fetch("/get_dashboard_data")
        .then(response => response.json())
        .then(data => {
            document.getElementById("totalBooks").innerText = data.total_books;
            document.getElementById("notReturnedBooks").innerText = data.not_returned;
            document.getElementById("issuedBooks").innerText = data.issued_books;
        });

    // Logout functionality
    document.getElementById("logoutBtn").addEventListener("click", function() {
        fetch("/logout", { method: "POST" })
            .then(() => {
                window.location.href = "/";  // Redirect to login page
            });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    fetchBooks();

    document.getElementById("home-tab").addEventListener("click", function() {
        showSection("home");
    });

    document.getElementById("dashboard-tab").addEventListener("click", function() {
        showSection("dashboard");
    });

    function showSection(sectionId) {
        document.querySelectorAll(".content").forEach(section => {
            section.style.display = "none";
        });
        document.getElementById(sectionId).style.display = "block";
    }

    function fetchBooks() {
        fetch("/get_books")
            .then(response => response.json())
            .then(data => {
                let bookList = document.getElementById("book-list");
                bookList.innerHTML = "";
                data.forEach(book => {
                    let row = `<tr>
                        <td>${book.title}</td>
                        <td>${book.author}</td>
                        <td>${book.year}</td>
                        <td><button onclick="borrowBook(${book.id})">Borrow</button></td>
                    </tr>`;
                    bookList.innerHTML += row;
                });
            });
    }

    window.borrowBook = function(bookId) {
        fetch(`/borrow/${bookId}`, { method: "POST" })
            .then(response => response.json())
            .then(data => alert(data.message));
    }
});
*/
document.addEventListener("DOMContentLoaded", function() {
    let currentPage = window.location.pathname;
    let navLinks = document.querySelectorAll("nav ul li a");

    navLinks.forEach(link => {
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }
    });
});

