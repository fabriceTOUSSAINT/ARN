import React from 'react';
import { createStackNavigator } from 'react-navigation-stack';

import Signup from '../screens/Signup';
import Signin from '../screens/Signin';

const MainStack = createStackNavigator(
    {
        Signup: {
            screen: Signup
        },
        Signin: {
            screen: Signin
        },
    },
    {
        initialRouteName: 'Signup'
    }
)

export default MainStack