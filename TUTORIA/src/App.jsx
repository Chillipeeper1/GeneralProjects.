import { useState } from 'react';
import './App.css';

function App() {
  
  const [inputValue, setInputValue] = useState('');
  
  const [submittedText, setSubmittedText] = useState('');

  const handleClick = async () => {
    
    const res = await fetch('http://127.0.0.1:8000/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: inputValue }),
    });
    const data = await res.json();
    setSubmittedText(data.answer);
  };

  return (
    
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100">
      
      <div>
        <input 
          type="text" 
          placeholder="Escribe algo..."
          
          value={inputValue}
         
          onChange={(e) => setInputValue(e.target.value)}
          style={{ width: "300px", height: "30px", padding: "8px" }}
        />
        <button onClick={handleClick} style={{ height: "55px", marginLeft: '20px' }}>
          Enter
        </button>
      </div>

      {submittedText && (
        <p style={{ marginTop: '20px' }}>
          Texto escrito: **{submittedText}**
        </p>
      )}

    </div>
  );
}

export default App;