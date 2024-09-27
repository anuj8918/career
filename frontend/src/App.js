// import React from 'react';
import UserProfileForm from './components/UserProfileForm';
import CareerRecommendations from './components/CareerRecommendations';
import UserResumeForm from './components/UserResumeForm';

function App() {
    const userId = 1;  // Replace with dynamic userId based on your setup

    return (
        <div>
            <h1>AI Career Path Advisor</h1>
            <UserProfileForm />
            <CareerRecommendations userId={userId} />
            <UserResumeForm userId={userId} />  {/* Add Resume Form */}
        </div>
    );
}

export default App;
