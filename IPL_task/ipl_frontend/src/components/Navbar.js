import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Link, useLocation } from 'react-router-dom';

const Navbar = () => {
  const location = useLocation();

  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" sx={{ flexGrow: 1 }}>
          IPL Dashboard
        </Typography>
        <Box>
          <Button
            color="inherit"
            component={Link}
            to="/"
            sx={{ backgroundColor: location.pathname === '/' ? 'rgba(255,255,255,0.1)' : 'transparent', marginRight: 1 }}
          >
            Home
          </Button>
          <Button
            color="inherit"
            component={Link}
            to="/extra-runs"
            sx={{ backgroundColor: location.pathname === '/extra-runs' ? 'rgba(255,255,255,0.1)' : 'transparent' }}
          >
            Extra Runs
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;

