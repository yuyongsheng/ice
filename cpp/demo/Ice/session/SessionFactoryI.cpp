// **********************************************************************
//
// Copyright (c) 2003-2005 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

#include <SessionFactoryI.h>
#include <ReapThread.h>

using namespace std;
using namespace Demo;

SessionPrx
SessionFactoryI::create(const string& name, const Ice::Current& c)
{
    SessionIPtr session = new SessionI(name);
    SessionPrx proxy = SessionPrx::uncheckedCast(c.adapter->addWithUUID(session));
    ReapThread::instance()->add(proxy, session);
    return proxy;
}

void
SessionFactoryI::shutdown(const Ice::Current& c)
{
    cout << "Shutting down..." << endl;
    c.adapter->getCommunicator()->shutdown();
}
