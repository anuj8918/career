import React, { useState } from 'react';
import axios from 'axios';

function UserResumeForm({ userId }) {
    const [resumeData, setResumeData] = useState({
        summary: '',
        education: '',
        experience: '',
        skills: ''
    });

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post(`http://localhost:5000/resume/${userId}`, resumeData)
            .then(response => alert("Resume created successfully!"))
            .catch(error => alert("Error creating resume."));
    };

    return (
        <form onSubmit={handleSubmit}>
            <textarea placeholder="Summary" value={resumeData.summary} onChange={(e) => setResumeData({ ...resumeData, summary: e.target.value })} />
            <textarea placeholder="Education" value={resumeData.education} onChange={(e) => setResumeData({ ...resumeData, education: e.target.value })} />
            <textarea placeholder="Experience" value={resumeData.experience} onChange={(e) => setResumeData({ ...resumeData, experience: e.target.value })} />
            <textarea placeholder="Skills" value={resumeData.skills} onChange={(e) => setResumeData({ ...resumeData, skills: e.target.value })} />
            <button type="submit">Submit Resume</button>
        </form>
    );
}

export default UserResumeForm;
