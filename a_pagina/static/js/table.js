function printTicket(url) {
  // Abre la URL en una nueva ventana
  const printWindow = window.open(url, "_blank");

  // Cuando la ventana termine de cargar, imprime
  printWindow.onload = function () {
    printWindow.print();
    // Espera un momento y luego cierra la ventana
    setTimeout(function () {
      printWindow.close();
    }, 5000); // Espera 1 segundo antes de cerrar
  };
}

function deleteTicket(ticketId) {
  const themeColor = document.querySelector('meta[name="theme-color"]');
  themeColor.setAttribute("content", "#991B1B");
  if (confirm("¿Estás seguro que deseas eliminar este ticket?")) {
    fetch(`/delete-ticket/${ticketId}/`, {
      method: "DELETE",
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
      .then((response) => {
        if (response.ok) {
          // Recarga la página después de eliminar
          window.location.reload();
          themeColor.setAttribute("content", "#0F172A");
        } else {
          alert("Error al eliminar el ticket");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Error al eliminar el ticket");
      });
  } else {
    themeColor.setAttribute("content", "#0F172A");
  }
}

// Función auxiliar para obtener el token CSRF
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
