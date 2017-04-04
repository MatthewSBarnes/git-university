def customer(env, name, mech, DAY_LENGTH, job_duration, status):
    arrive = env.now
    # Request one of the servers
    print('ARR\t%s arriving at %d\t|| job_duration: %d' % (name, arrive, job_duration))

    if (status == 1):
        print('BYE\tSending %s home' % (name)) 

    else:
        with mech.request() as req:
            yield req

            wait = env.now - arrive
            print('SER\t%s being served at %d' % (name, env.now))

            yield env.timeout(job_duration)
            print('FIN\t%s finished being served at %d' % (name, env.now))
