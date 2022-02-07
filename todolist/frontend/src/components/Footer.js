import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';


const Footer = () => {
    return (
        <footer className='footer-copyright fixed-bottom text-center bg-light py-3'>
            &copy; {new Date().getFullYear()} Copyright: <a className='text-decoration-none' href='https://www.linkedin.com/in/anatolytsi'> Ivanov Aleksandr </a>
        </footer>
    )
}

export default Footer
