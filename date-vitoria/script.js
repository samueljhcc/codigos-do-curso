const no=document.getElementById('no');
no.onmouseover=()=>{no.style.position='fixed';no.style.left=Math.random()*(innerWidth-100)+'px';no.style.top=Math.random()*(innerHeight-50)+'px';};
yes.onclick=()=>{music.play().catch(()=>{});q.classList.add('hidden');d.classList.remove('hidden');confetti();};
confirm.onclick=()=>{if(!date.value||!time.value){alert('Escolha data e horário');return;}
const txt=`Resposta do convite\n\nPara: Vitória\nResposta: Sim\nData: ${date.value}\nHorário: ${time.value}\n\nAgora é só esperar! ❤️`;
const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([txt],{type:'text/plain'}));a.download='resposta_vitoria.txt';a.click();
d.classList.add('hidden');done.classList.remove('hidden');};
function confetti(){const c=document.getElementById('confetti'),x=c.getContext('2d');c.width=innerWidth;c.height=innerHeight;let p=[...Array(150)].map(()=>({x:Math.random()*c.width,y:-20,r:5+Math.random()*5,vy:2+Math.random()*4,vx:-2+Math.random()*4}));
(function anim(){x.clearRect(0,0,c.width,c.height);p.forEach(o=>{o.x+=o.vx;o.y+=o.vy;x.fillRect(o.x,o.y,o.r,o.r);});p=p.filter(o=>o.y<c.height+20);if(p.length)requestAnimationFrame(anim);})();}