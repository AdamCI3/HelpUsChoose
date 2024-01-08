import { useState ,useEffect } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  useEffect(()=>{
    async function fetchData(){
    console.log(import.meta.env.VITE_API_URL)
    try{
      // const response = await fetch(`${import.meta.env.VITE_API_URL}init`,{credentials: "same-origin"});
      const response = await fetch("api/init",{credentials: "include"});
      if(!response.ok)
      {
        throw new Error('Network response was not ok');
      }
      const result = await response.json()
      console.log(result)
    }catch(error)
    {
      console.error('Error fetching data: ',error)
    }
  }
    fetchData();
  },[])
  return (
    <>
    hello world
    </>
  )
}

export default App
