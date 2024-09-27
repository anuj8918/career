import React, { useEffect, useState } from 'react';
import axios from 'axios';

function CareerRecommendations({ userId }) {
    const [recommendations, setRecommendations] = useState([]);

    useEffect(() => {
        axios.get(`http://localhost:5000/recommendations/${userId}`)
            .then(response => setRecommendations(response.data.recommendations))
            .catch(error => console.error(error));
    }, [userId]);

    return (
        <div>
            <h2>Career Recommendations</h2>
            <ul>
                {recommendations.map((rec, index) => (
                    <li key={index}>{rec}</li>
                ))}
            </ul>
        </div>
    );
}

export default CareerRecommendations;
