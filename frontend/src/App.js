import useCookie from 'react-use-cookie';
import logo from './logo.svg';
import './App.css';
import ContentTable from './ContentTable.js';

function App() {
  const [token, setUserToken] = useCookie('dj_token');

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        {!token && <a
            className="App-link"
            href="http://localhost:8000/api/v1/init_hs_oauth/"
          >
            Sign In with HubSpot
          </a>
        }
        {token && <ContentTable token={token}/>}

      </header>
    </div>
  );
}

export default App;
