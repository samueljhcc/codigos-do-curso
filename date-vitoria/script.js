const screens=['screen1','screen2','screen3','screen4'];
function show(id){screens.forEach(s=>document.getElementById(s).classList.add('hidden'));document.getElementById(id).classList.remove('hidden');}

noBtn.addEventListener('mouseover',()=>{
 noBtn.style.position='fixed';
 noBtn.style.left=Math.random()*(innerWidth-120)+'px';
 noBtn.style.top=Math.random()*(innerHeight-50)+'px';
});

yesBtn.onclick=()=>{
 music.play().catch(()=>{});
 show('screen2');
};

continueBtn.onclick=()=>{
 if(!date.value||!time.value){alert('Escolha data e horário');return;}
 summary.textContent=`Data: ${date.value} | Horário: ${time.value}`;
 show('screen3');
};

backBtn.onclick=()=>show('screen2');

confirmBtn.onclick=()=>{
 const txt=`Para: Vitória\nData: ${date.value}\nHorário: ${time.value}\n\nAgora é só esperar!`;
 const blob=new Blob([txt],{type:'text/plain'});
 const a=document.createElement('a');
 a.href=URL.createObjectURL(blob);
 a.download='resposta_vitoria.txt';
 a.click();
 show('screen4');
};