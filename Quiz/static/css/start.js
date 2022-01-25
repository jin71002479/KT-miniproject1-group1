const main=document.querySelector("#main")
const qna=document.querySelector("#qna")
const result=document.querySelector('#result')
const endPoint=10
const select=[];
const answer=[1,2,0,1,1,0,2,2,0,2]

function setResult()
{
    var count=0
    var imgURL

    for (var i=0;i<select.length;i++)
    {
        if(select[i]==answer[i])
            count++
    }
    
    if(count==endPoint)
        imgURL= "/static/css/gold.png";
    else if(count>5)
        imgURL= "/static/css/silver.png";
    else
        imgURL= "/static/css/bronze.png";
    
    const resultName=document.querySelector('.resultname')
    resultName.innerHTML=infoList[count].name

    var resultImg=document.createElement('img')
    const imgDiv=document.querySelector('#resultImg')
    
    resultImg.src= imgURL
    console.log(resultImg)
    imgDiv.appendChild(resultImg);

    const resultDesc=document.querySelector('.resultDesc');
    resultDesc.innerHTML=infoList[count].desc;
    console.log(count)
    document.getElementById("mycount").value = count*10;
}

function goResult()
{
    
    var r=document.querySelector('.resultname');
    qna.style.WebkitAnimation="fadeOut 1s"
    qna.style.animation="fadeOut 1s"
    setTimeout(()=>{
        result.style.WebkitAnimation="fadeIn 1s"
        result.style.animation="fadeIn 1s"
        setTimeout(()=>{
            qna.style.display="none"
            result.style.display="block"
        },450)})
        console.log(select)
        setResult()
}

function addAnswer(answerText,qIdx,Idx)
{
    var a= document.querySelector('.answerBox');
    var answer=document.createElement('button');
    answer.classList.add('answerList');
    answer.classList.add('my-3');
    answer.classList.add('py-3');
    answer.classList.add('mx-auto');
    answer.classList.add('fadeIn');

    a.appendChild(answer);
    answer.innerHTML = answerText;
    answer.addEventListener("click", function(){
        var children = document.querySelectorAll('.answerList');
        for(let i=0; i<children.length;i++)
        {
            children[i].disabled=true;
            children[i].style.WebkitAnimation="fadeOut 1s";
            children[i].style.animation="fadeOut 1s";
        }
        setTimeout(() => {
            select[qIdx]=Idx; 
            for(let i=0; i<children.length;i++){
            children[i].style.display='none';
            }
            goNext(++qIdx);
        }, 450);     
        
    }, false);
}

function goNext(qIdx)
{
  if(qIdx==endPoint){
        goResult();
        return;
  }
  var q=document.querySelector('.qBox');
  q.innerHTML=qnaList[qIdx].q;
  for(let i in qnaList[qIdx].a){
      addAnswer(qnaList[qIdx].a[i].answer,qIdx,i);
  }
  var status= document.querySelector('.statusBar')
  status.style.width=(100/endPoint)*(qIdx)+'%';
  
}

function begin()
{
    main.style.WebkitAnimation="fadeOut 1s"
    main.style.animation="fadeOut 1s"
    setTimeout(()=>{
        
        qna.style.WebkitAnimation="fadeIn 1s"
        qna.style.animation="fadeIn 1s"
    
    setTimeout(()=>{
        main.style.display="none"
        qna.style.display="block"
        },450)
        let qIdx=0;
        goNext(qIdx);
    },450);
    
}