import React, { useState } from 'react';
import axios from 'axios';

function UserProfileForm() {
    const [userData, setUserData] = useState({
        name: '',
        email: '',
        skills: '',
        interests: ''
    });

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post('http://localhost:5000/user', { 
            ...userData, 
            skills: userData.skills.split(','), 
            interests: userData.interests.split(',') 
        })
        .then(response => alert("User created successfully!"))
        .catch(error => alert("Error creating user."));
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Name" onChange={(e) => setUserData({ ...userData, name: e.target.value })} />
            <input type="email" placeholder="Email" onChange={(e) => setUserData({ ...userData, email: e.target.value })} />
            <input type="text" placeholder="Skills (comma-separated)" onChange={(e) => setUserData({ ...userData, skills: e.target.value })} />
            <input type="text" placeholder="Interests (comma-separated)" onChange={(e) => setUserData({ ...userData, interests: e.target.value })} />
            <button type="submit">Submit Profile</button>
        </form>
    );
}

export default UserProfileForm;
