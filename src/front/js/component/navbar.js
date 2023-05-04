import React from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import { useContext } from "react";
import { useNavigate } from 'react-router-dom';

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	const navigate = useNavigate()
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="ml-auto">
					{!store.token ? 
					<Link to="/login">
						<button className="btn btn-primary">Login</button>
					</Link>
					:
					<button onClick={() => {actions.logout(); navigate('/signup')}} className="btn btn-primary">Logout</button>
					}
				</div>
			</div>
		</nav>
	);
};
