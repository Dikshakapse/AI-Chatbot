import React, { useState } from "react";
import axios from "axios";
import { 
    Container, 
    TextField, 
    Button, 
    Typography, 
    List, 
    ListItem, 
    ListItemText, 
    Paper, 
    Box, 
    AppBar, 
    Toolbar, 
    CssBaseline 
} from "@mui/material";
import { createTheme, ThemeProvider } from "@mui/material/styles";

const theme = createTheme({
    palette: {
        primary: {
            main: "#D2B48C", 
        },
        secondary: {
            main: "#E6D5B8", 
        },
        background: {
            default: "#F5F5DC", 
            paper: "#FFFFFF",  
        },
        text: {
            primary: "#333333", 
            secondary: "#666666", 
        },
    },
    typography: {
        fontFamily: "'Roboto', sans-serif",
        h4: {
            fontWeight: 600,
            color: "#333333", 
        },
        body1: {
            color: "#333333", 
        },
    },
});



function App() {
    const [query, setQuery] = useState("");
    const [responses, setResponses] = useState([]);

    const handleQuery = async () => {
        try {
            const response = await axios.post("http://localhost:8000/query", { query });
            setResponses([...responses, { query, response: response.data.response }]);
        } catch (error) {
            console.error("Error fetching data:", error);
            setResponses([...responses, { query, response: "Error: Unable to fetch data." }]);
        }
    };

    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="h6">AI-Powered Chatbot</Typography>
                </Toolbar>
            </AppBar>
            <Container maxWidth="md" sx={{ mt: 4, mb: 4 }}>
                <Paper elevation={3} sx={{ p: 3, backgroundColor: "background.paper" }}>
                    <Typography variant="h4" gutterBottom align="center" color="primary">
                        Supplier and Product Information
                    </Typography>
                    <Box sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
                        <TextField
                            fullWidth
                            label="Enter your query"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            variant="outlined"
                            margin="normal"
                        />
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleQuery}
                            sx={{ alignSelf: "center", width: "200px" }}
                        >
                            Submit
                        </Button>
                    </Box>
                    <List sx={{ mt: 3 }}>
                        {responses.map((item, index) => (
                            <ListItem key={index} sx={{ mb: 2 }}>
                                <Paper elevation={2} sx={{ p: 2, width: "100%" }}>
                                    <ListItemText
                                        primary={`You: ${item.query}`}
                                        secondary={`Bot: ${JSON.stringify(item.response, null, 2)}`}
                                        primaryTypographyProps={{ color: "primary" }}
                                        secondaryTypographyProps={{ color: "text.secondary" }}
                                    />
                                </Paper>
                            </ListItem>
                        ))}
                    </List>
                </Paper>
            </Container>
        </ThemeProvider>
    );
}

export default App;