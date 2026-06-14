const noBtn=document.getElementById('noBtn');
const yesBtn=document.getElementById('yesBtn');
const confirmBtn=document.getElementById('confirmBtn');

const questionPage=document.getElementById('questionPage');
const datePage=document.getElementById('datePage');
const successPage=document.getElementById('successPage');

const music=document.getElementById('music');
const dateInput=document.getElementById('date');
const timeInput=document.getElementById('time');

noBtn.addEventListener('mouseover',()=>{
    noBtn.style.position='fixed';
    noBtn.style.left=Math.random()*(window.innerWidth-100)+'px';
    noBtn.style.top=Math.random()*(window.innerHeight-50)+'px';
});

yesBtn.addEventListener('click',()=>{
    music.play().catch(()=>{});
    questionPage.classList.add('hidden');
    datePage.classList.remove('hidden');
});

confirmBtn.addEventListener('click',()=>{
    if(!dateInput.value || !timeInput.value){
        alert('Escolha uma data e um horário.');
        return;
    }

    const conteudo=`Resposta do convite\n\nPara: Vitória\nData: ${dateInput.value}\nHorário: ${timeInput.value}\n\nAgora é só esperar! ❤️`;

    const blob=new Blob([conteudo],{type:'text/plain'});
    const link=document.createElement('a');
    link.href=URL.createObjectURL(blob);
    link.download='resposta_vitoria.txt';
    link.click();

    datePage.classList.add('hidden');
    successPage.classList.remove('hidden');
});