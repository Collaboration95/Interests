
import './App.css';

function Generate(){ 
  
  let element = [1,2,3,4,5,6,7]

  return(<div className="boxes">{element.map(name=><button key={name}>{name}</button>)}</div>)
}
export default Generate;

fetch('CurrentLinks.txt').then(response=>response.text()).then(data=>{
  console.log(data)
})