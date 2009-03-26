// **********************************************************************
//
// Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

#ifndef GREET_ICE
#define GREET_ICE

module Demo
{

["java:serializable:Demo.MyGreeting"] sequence<byte> Greeting;

interface Greet
{
    idempotent void sendGreeting(Greeting g);
    void shutdown();
};

};

#endif
