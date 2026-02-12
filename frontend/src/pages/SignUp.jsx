import { Box, Button, Typography, InputAdornment, IconButton, TextField } from '@mui/material'
import { Visibility, VisibilityOff, Email, PermIdentity } from '@mui/icons-material'
import { Link as RouterLink } from 'react-router-dom'
import { useState } from 'react'
import AuthFormLayout from '../components/layout/AuthFormLayout'
import logo from '../assets/logo.png'

export default function SignUp() {
  const [showPassword, setShowPassword] = useState(false)
  //password use
  //email use
  //username use
  
  return (
    <AuthFormLayout>
      <Box
        sx={{
          p: { xs: 4, md: 6 },
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <Box
          component="img"
          src={logo}
          alt="Suntsy logo"
          sx={{ width: 144, mb: 3 }}
        />

        <Typography variant="h4" 
          sx={{
            mb: 1,
            fontSize: '28px',
            width: 400, 
            height: 48, 
          }}>
          Create your Suntsy account
        </Typography>


        <Box sx={{ width: '100%', maxWidth: 420 }}>
          <TextField
            placeholder="Email"
            fullWidth
            sx={{ mb: 2 }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <Email />
                </InputAdornment>
              ),
            }}
          />

          <TextField
            placeholder="Username"
            fullWidth
            sx={{ mb: 2 }}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <PermIdentity />
                </InputAdornment>
              ),
            }}
          />

        <TextField
          placeholder="Password"
          type={showPassword ? 'text' : 'password'}
          fullWidth
          sx={{ mb: 4 }}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton
                  onClick={() => setShowPassword(!showPassword)}
                  edge="end"
                >
                  {showPassword ? <VisibilityOff /> : <Visibility />}
                </IconButton>
              </InputAdornment>
            ),
          }}
        />

        <Button
          variant="suntsy"
          component={RouterLink}
          to="/"
          fullWidth
          sx={{
            fontSize: '20px',
            height: 44,
          }}
        >
          Register
        </Button>

      </Box>

      </Box>

    </AuthFormLayout>
  )
}