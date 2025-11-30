import logo from './logo.svg';
import './App.css';

// TODO query users and list them out.


console.log(`react environment`)
console.log(process.env);


function App() {
  console.log('app');
  console.log(process.env);
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <a
                  className="App-link"

          href="/static-html"
        >
          static-html
        </a>

        <a
                  className="App-link"

          href="/api/users"
        >
          get users api-request
        </a>
      </header>
    </div>
  );
}

export default App;
