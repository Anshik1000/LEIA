
const questions = [
    {
        question: "Are you aware of any metacognition techniques?",
        answers: [
            { text: "Yes", turtle: 4, dolphin: 0, elephant: 0, owl: 4 },
            { text: "No", turtle: 0, dolphin: 4, elephant: 4, owl: 0 }
        ]
    },
    {
        question: "How many hours do you study throughout the day?",
        answers: [
            { text: "1-2 hours", turtle: 0, dolphin: 0, elephant: 0, owl: 5 },
            { text: "2-3 hours", turtle: 3, dolphin: 3, elephant: 3, owl: 2 },
            { text: "3+ hours", turtle: 4, dolphin: 0, elephant: 4, owl: 2 },
            { text: "less than 1 hour", turtle: 0, dolphin: 4, elephant: 0, owl: 2 }
        ]
    },
    {
        question: "If you use any of the metacognition techniques, how often do you stick to it?",
        answers: [
            { text: "Often", turtle: 2, dolphin: 0, elephant: 0, owl: 2 },
            { text: "Not often", turtle: 2, dolphin: 0, elephant: 0, owl: 4 },
            { text: "I don't know such techniques", turtle: 0, dolphin: 3, elephant: 3, owl: 0 }
        ]
    },
    {
        question: "Do you rely on one method of learning a lot, such as re-reading textbooks, etc.?",
        answers: [
            { text: "Yes", turtle: 0, dolphin: 4, elephant: 4, owl: 0 },
            { text: "No", turtle: 2, dolphin: 0, elephant: 0, owl: 4 }
        ]
    },
    {
        question: "Do you learn out of syllabus or curriculum on whatever you are learning?",
        answers: [
            { text: "Yes", turtle: 5, dolphin: 0, elephant: 0, owl: 0 },
            { text: "No", turtle: 0, dolphin: 2, elephant: 2, owl: 2 }
        ]
    },
    {
        question: "Do you face difficulty looking at the big picture of something you are learning?",
        answers: [
            { text: "Yes", turtle: 4, dolphin: 0, elephant: 4, owl: 0 },
            { text: "No", turtle: 0, dolphin: 4, elephant: 0, owl: 4 }
        ]
    },
    {
        question: "Do you learn most of your things from your friends, colleagues?",
        answers: [
            { text: "Yes", turtle: 2, dolphin: 5, elephant: 0, owl: 0 },
            { text: "No", turtle: 0, dolphin: 0, elephant: 2, owl: 2 }
        ]
    },
    {
        question: "Do you face trouble memorizing items?",
        answers: [
            { text: "Yes", turtle: 3, dolphin: 3, elephant: 0, owl: 0 },
            { text: "No", turtle: 0, dolphin: 0, elephant: 5, owl: 3 }
        ]
    },
    {
        question: "Do you often rely on memorizing the things you are learning?",
        answers: [
            { text: "Yes", turtle: 0, dolphin: 3, elephant: 4, owl: 2 },
            { text: "No", turtle: 3, dolphin: 0, elephant: 0, owl: 2 }
        ]
    },
    {
        question: "What are your views on learning?",
        answers: [
            { text: "I like to learn but I don't feel like learning on my own or cannot give time to learning", turtle: 2, dolphin: 4, elephant: 0, owl: 0 },
            { text: "I like to learn and I am actively giving some time of my day for learning.", turtle: 2, dolphin: 0, elephant: 0, owl: 3 },
            { text: "I do not like learning", turtle: 0, dolphin: 0, elephant: 4, owl: 0 }
        ]
    }
];
const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btn");
const signUp= document.getElementById("sign-up")
const signUpPage = document.getElementById('lsignup')
let currentQuestionIndex=0;
let turtle=0;
let elephant=0;
let owl=0;
let dolphin=0;
let result='Dolphin';
function startQuiz(){
    currentQuestionIndex=0
    turtle=0;
    elephant=0;
    owl=0;
    dolphin=0;
    nextButton.innerHTML="Next";
    showQuestion();
}

function showQuestion(){
    resetState();
    let currentQuestion= questions[currentQuestionIndex];
    let questionNo = currentQuestionIndex +1;
    questionElement.innerHTML = questionNo+". "+currentQuestion.question;

    currentQuestion.answers.forEach(answer=>{
        const button= document.createElement("button");
        button.innerHTML=answer.text;
        button.classList.add("btn");
        button.dataset.turtle = answer.turtle;
        button.dataset.dolphin = answer.dolphin;
        button.dataset.elephant = answer.elephant;
        button.dataset.owl = answer.owl; // adding answer to the button's property.
        answerButtons.appendChild(button);
        
      
        button.addEventListener("click",selectAnswer);

    })


}
function showResult(){
    resetState();
    const heading= document.getElementById("result");
    heading.innerHTML="You are:"

    if(turtle>Math.max(dolphin,elephant,owl) )
    {
        questionElement.innerHTML='Turtle:The Deep Diver';
        const learnertype=document.getElementById('turtle');
        learnertype.style.display='block';
        // for sign up
        result = 'Turtle';

    }
    else if(dolphin>Math.max(elephant,owl,turtle)){
        questionElement.innerHTML='Dolphin:The Social Scholar';
        const learnertype=document.getElementById('Dolphin');
        learnertype.style.display='block';
        result = 'Dolphin'; // for sign up


    }
    else if(elephant>Math.max(dolphin,owl,turtle)){
        questionElement.innerHTML='Elephant:The Memory Maestro';
        const learnertype=document.getElementById('elephant');
        learnertype.style.display='block';
        result = 'Elephant'; // for sign up


    }
    else if(owl>Math.max(elephant,dolphin,turtle)){
        questionElement.innerHTML='Owl:The Metacognitive Master';
        const learnertype=document.getElementById('owl');
        learnertype.style.display='block';
        result = 'Owl'; // for sign up


    }
    else
    {
        alert("error there might be equal points");
        alert(turtle)
        alert(owl)
        alert(elephant)
        alert(dolphin)
    }
    signUp.style.display ='block';
    

}


function resetState(){
    nextButton.style.display="none";
    while(answerButtons.firstChild){
        answerButtons.removeChild(answerButtons.firstChild);
    }
}
function handleNextButton(){
    currentQuestionIndex++;
    if(currentQuestionIndex<questions.length){
        showQuestion();
    }
    else{
        showResult();
        
    }
}


function selectAnswer(e){

    const selectedButton = e.target;
    turtle = turtle + selectedButton.dataset.turtle;
    dolphin = dolphin + selectedButton.dataset.dolphin;
    owl = owl + selectedButton.dataset.owl;
    elephant = elephant + selectedButton.dataset.elephant;
    selectedButton.classList.add("selected");

    Array.from(answerButtons.children).forEach(button=>{
        button.disabled=true;
        if(button!=selectedButton){
            button.style.display = "none";
            

        }
       
    });
  
    
    nextButton.style.display = "block";
    
}
//below function gets edited when they start signing up i.e this function should affect signup.html here result is a string which will come from showresult.
function signupedit(){
    const quizsection = document.getElementById('quiz');
    quizsection.style.display = "none";
    signUpPage.style.display = "block";
    const Learn = document.getElementById("Learner");
    Learn.value= result;
    Learn.disabled=true;

}

nextButton.addEventListener("click",()=>{
    if(currentQuestionIndex<questions.length){
        handleNextButton();
    }else{
        nextButton.style.display = "none";
        signUp.style.display='block';
    }
})

signUp.addEventListener("click",signupedit)
startQuiz()

