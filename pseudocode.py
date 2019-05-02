"""
pseudo code / flow


param - loops
param - meal

// from customer answers, keep only those that match meal features

// convo opens with waiter greeting

// build convo
while loops > 0

    reply = customer(reply)
    reply = waiter(reply)
    loops--



// waiter and customer functions construct replies. if prev_reply contains questions, picks eligible reply.
// picks eligible follow up question (sometimes? always?)
def waiter(prev_reply)

    question = none
    answer = none

    //unpack reply
    if reply has answer
        //check answer type
        if greeting
            question = pick random starter question
        elseif info
            remove questions and answers based on info in answer and speaker


    if reply has question
        // check question type
        if greeting
            answer = pick random greeting answer from domain

        if RFI
            answer = pick random answer from question domain where speaker = waiter

        if clarify
            answer = repeat previous question(????), different versions of same questions(????)

    return reply = (answer, question)


def customer(prev_reply)


    question = none
    answer = none

    //unpack reply
    if reply has answer
        if greeting
            question = pick random starter question
        elseif info
            remove questions and answers based on info in answer


"""