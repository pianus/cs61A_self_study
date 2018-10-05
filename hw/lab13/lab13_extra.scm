; Q4
(define (rle s)
  (define (helper s last numb)
    (cond ((and (null? s) (null? last)) nil)
          ((null? s) (cons-stream (list last numb) nil))
          (else (if (eq? (car s) last)
                    (helper (cdr-stream s) (car s) (+ numb 1))
                    (if (null? last)
                        (helper (cdr-stream s) (car s) 1)
                        (cons-stream (list last numb)
                                 (helper (cdr-stream s) (car s) 1)))))))
  (helper s nil nil)
)

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  (define (helper lst1 n s)
    (cond ((null? s) (append lst1 (list n)))
          ((<= n (car s)) (append lst1 (cons n s)) )
          (else (helper (append lst1 (list (car s))) n (cdr s)))))
  (helper nil n s)
)

; Q6
(define (deep-map fn s)
  (cond ((null? s) nil)
        (else (if (list? (car s))
                  (cons (deep-map fn (car s)) (deep-map fn (cdr s)))
                  (cons (fn (car s)) (deep-map fn (cdr s))))))
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  (define (in? name s)
    (cond ((null? s) #f)
          ((eq? (car s) name) #t)
          (else (in? name (cdr s)))))
  (define (helper s lst)
    (cond ((null? s) lst)
          ((in? (car s) lst) (helper (cdr s) lst))
          (else (helper (cdr s) (append lst (list (car s)))))))
  (helper s nil)
)

(define (count name s)
  (cond ((null? s) 0)
        ((eq? name (car s)) (+ 1 (count name (cdr s))))
        (else (count name (cdr s))))
)

(define (tally names)
  (map (lambda (name) (cons name (count name names))) (unique names))
)
