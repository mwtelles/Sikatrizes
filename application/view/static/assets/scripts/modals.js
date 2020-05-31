function like() {
    Swal.fire(
        'Você curtiu!',
        'Obrigado pelo feedback!',
        'success'
    )
}

function deslike() {
    Swal.fire(
        'Que pena!',
        'Obrigado pelo feedback!',
        'error'
    )
}

function comment() {
    Swal.fire({
        title: 'Digite seu usuário do Github',
        input: 'text',
        inputAttributes: {
            autocapitalize: 'off'
        },
        showCancelButton: true,
        confirmButtonText: 'Enviar',
        showLoaderOnConfirm: true,
        preConfirm: (login) => {
            return fetch(`//api.github.com/users/${login}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(response.statusText)
                    }
                    return response.json()
                })
                .catch(error => {
                    Swal.showValidationMessage(
                        `Request failed: ${error}`
                    )
                })
        },
        allowOutsideClick: () => !Swal.isLoading()
    }).then((result) => {
        if (result.value) {
            Swal.fire({
                title: `avatar de ${result.value.login}`,
                imageUrl: result.value.avatar_url
            })
        }
    })
}