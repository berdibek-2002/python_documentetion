const readlineSync = require('readline-sync');

console.log("******************************************************************************* \n" +
    "* Don-don ziki o'yiniga xush kelibsiz! Quyidagi variantlardan birini tanlang. (yakunlash uchun 'stop' yozing!) * \n" +
    "*******************************************************************************");

function determineWinner(playerChoice, computerChoice) {
    if (playerChoice === computerChoice) {
        return "Durrang!";
    } else if ((playerChoice === "Tosh" && computerChoice === "Qog'oz") ||
        (playerChoice === "Qog'oz" && computerChoice === "Qaychi") ||
        (playerChoice === "Qaychi" && computerChoice === "Tosh")) {
        return `Yutdingiz! ${playerChoice} ustun ${computerChoice}`;
    } else {
        return `Yutqazdingiz! ${playerChoice} yopib qo'ydi ${computerChoice}`;
    }
}

function playGame() {
    const choices = ["Tosh", "Qog'oz", "Qaychi"];
    let compScore = 0;
    let playerScore = 0;

    while (true) {
        const playerChoice = readlineSync.question("Tosh, Qog'oz, Qaychi?\n").charAt(0).toUpperCase() +
            readlineSync.question("Tosh, Qog'oz, Qaychi?\n").slice(1);

        if (playerChoice === 'Tugat' || playerChoice === "Stop") {
            console.log("Yakuniy hisob:");
            console.log(`Computer: ${compScore}`);
            console.log(`O'yinchi: ${playerScore}`);

            if (compScore > playerScore) {
                console.log("Kompyuter yutdi! Afsus... Yana urinib ko'ring.");
            } else if (compScore < playerScore) {
                console.log("O'yinchi g'olib! Tabriklaymiz!");
            } else {
                console.log("Durrang!");
            }
            break;
        }

        if (!choices.includes(playerChoice)) {
            console.log("Noto'g'ri tanlov! Iltimos, Tosh, Qog'oz yoki Qaychi tanlang.");
            continue;
        }

        const computerChoice = choices[Math.floor(Math.random() * choices.length)];
        const result = determineWinner(playerChoice, computerChoice);

        console.log(result);

        if (result.includes("Yutdingiz")) {
            playerScore++;
        } else if (result.includes("Yutqazdingiz")) {
            compScore++;
        }
    }
}

playGame();