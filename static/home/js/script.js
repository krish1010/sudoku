let original_board = []
window.onload = function () {
    for (let i = 0; i < 81; i++) {
        original_board.push(document.getElementById(String(i)).innerText)
    }
}

function foo(identifier) {
    let a = []
    for (let i = 0; i < 81; i++) {
        a.push(document.getElementById(String(i)).innerText)
    }
    if (identifier === 'solve')
        a = original_board
    const data = {board: a, job: identifier};

    fetch('/solve', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then(data => {
            bar(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function bar(data) {
    if ("status" in data) {
        if (data.status === false) {
            swal({
                title: "Nope!",
                text: "Your solution was not correct!",
                icon: "error",
                button: "Keep trying",
            });
        } else {
            swal({
                title: "Well done!",
                text: "Your solution was correct!",
                icon: "success",
                button: "Alright",
            });

        }
    } else {
        let index = 0
        for (let i = 0; i < 9; i++) {
            for (let j = 0; j < 9; j++) {
                document.getElementById(String(index)).innerText = data.solution[i][j]
                index = index + 1
            }
        }
    }
}

function checkNumber(id, evt) {
    const charCode = (evt.charCode)
    return !(charCode < 49 || charCode > 57) && !(document.getElementById(id).innerText.length > 0);
}

function resetBoard() {
    for (let i = 0; i < 81; i++) {
        document.getElementById(String(i)).innerText = original_board[i]
    }
    swal({
        title: "Board reset!",
        icon: "info",
    });
}

function newBoard() {
    swal("Loading a new one for you right away!");
    location.reload();
}

function startTime(){

}