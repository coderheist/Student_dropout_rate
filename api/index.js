/**
 * Vercel Node.js serverless function for student dropout prediction
 * Zero dependencies, rule-based prediction
 */

module.exports = (req, res) => {
    // Set CORS headers
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
    res.setHeader('Content-Type', 'application/json');
    
    // Handle CORS preflight
    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }
    
    // Handle GET (health check)
    if (req.method === 'GET') {
        const response = {
            status: 'working',
            message: 'Student Dropout Prediction API',
            runtime: 'Node.js',
            timestamp: new Date().toISOString()
        };
        res.status(200).json(response);
        return;
    }
    
    // Handle POST (prediction)
    if (req.method === 'POST') {
        try {
            const { features = [] } = req.body || {};
            
            // Simple prediction logic
            let prediction = 1; // Default: at risk
            let probability = 0.5;
            
            if (features.length > 6) {
                try {
                    const grade = parseFloat(features[6]) || 140;
                    if (grade > 150) {
                        prediction = 0; // Graduate
                        probability = 0.8;
                    } else {
                        prediction = 1; // At risk
                        probability = 0.7;
                    }
                } catch (e) {
                    // Use defaults
                }
            }
            
            const result = {
                prediction,
                probability,
                message: prediction === 0 ? 'Graduate' : 'At Risk',
                method: 'rule-based'
            };
            
            res.status(200).json(result);
            
        } catch (error) {
            const errorResponse = {
                error: error.message,
                prediction: 1,
                probability: 0.5,
                message: 'At Risk'
            };
            res.status(500).json(errorResponse);
        }
        return;
    }
    
    // Method not allowed
    res.status(405).json({ error: 'Method not allowed' });
};