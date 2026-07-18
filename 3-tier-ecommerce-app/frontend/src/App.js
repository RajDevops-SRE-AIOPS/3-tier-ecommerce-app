import React,{useEffect,useState} from 'react';
import './App.css';

function App(){

const [products,setProducts]=useState([]);

useEffect(()=>{
fetch("http://localhost:5000/products")
.then(res=>res.json())
.then(data=>setProducts(data));
},[]);

return(

<div className="container">

<h1>Simple E-Commerce Store</h1>

{
products.map(product=>(
<div className="card" key={product.id}>

<h2>{product.name}</h2>

<p>₹ {product.price}</p>

<button>Add To Cart</button>

</div>
))
}

</div>

);

}

export default App;
