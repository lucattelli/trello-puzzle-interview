# trello-puzzle-interview
Solving the Trello Puzzle

I did this to answer a job posting @ Trello in 2015.

## The programming Puzzle
Originally posted on http://web.archive.org/web/20141209192900/https://trello.com/jobs/developer and when I got mine, it didn't require you to write in JavaScript, so I wrote mine in Python.

Write JavaScript (or CoffeeScript) code to find a 9 letter string of characters that contains only letters from

```acdegilmnoprstuw```

such that the hash(the_string) is

```956446786872726```

if hash is defined by the following pseudo-code:

```
Int64 hash (String s) {
    Int64 h = 7
    String letters = "acdegilmnoprstuw"
    for(Int32 i = 0; i < s.length; i++) {
        h = (h * 37 + letters.indexOf(s[i]))
    }
    return h
}
```

For example, if we were trying to find the 7 letter string where ```hash(the_string)``` was ```680131659347```, the answer would be ```"leepadg"```.

To apply, please email jobs@trello.com with your solution as the first word in the subject line. Include any code you used to solve the problem as an attachment, and also send us a current resume in HTML, Plain Text, or PDF format. In the body of the email please explain why you would be a good fit for this job. If you have a website, send us the URL!
