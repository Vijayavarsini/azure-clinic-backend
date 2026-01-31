// Use relative URLs for API calls (same origin as the deployed app)
const API = window.location.origin;

function loadPatients() {
    fetch(`${API}/patients`)
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("patients");
            table.innerHTML = "";
            data.forEach(p => {
                table.innerHTML += `
                    <tr>
                        <td>${p.id}</td>
                        <td>${p.name}</td>
                        <td>${p.age}</td>
                        <td>${p.gender || ""}</td>
                        <td>${p.phone || ""}</td>
                        <td>
                            <button onclick="deletePatient(${p.id})">Delete</button>
                        </td>
                    </tr>
                `;
            });
        });
}

function addPatient() {
    const data = {
        name: document.getElementById("name").value,
        age: document.getElementById("age").value,
        gender: document.getElementById("gender").value,
        phone: document.getElementById("phone").value
    };

    fetch(`${API}/patients`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    }).then(() => {
        loadPatients();
    });
}

function deletePatient(id) {
    fetch(`${API}/patients/${id}`, { method: "DELETE" })
        .then(() => loadPatients());
}

loadPatients();