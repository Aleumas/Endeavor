export interface Concepts {
    value: string[],
    tags: string[]
}

export interface Question {
    text: string,
    response: string
}

export interface Feedback {
    value: {
        question: string,
        feedback: string
    }
    rating: number
}