(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))
(define (cadar x) (car (cdr (car x))))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  'replace-this-line)

(define (zip lst)
(if (null? lst)
    '(nil nil)
    (list (cons (caar lst) (car (zip (cdr lst))))
          (cons (cadar lst) (cadr (zip (cdr lst)))))))


;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (helper s k)
          (if (null? s)
              nil
              (cons (cons k (cons (car s) nil)) (helper (cdr s) (+ k 1))))
          )
  (helper s 0))
  ; END PROBLEM 17

;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change n lst)
  (define (cons-all first rests)
    (if (null? rests)
        nil
        (map (lambda (lst1) (cons first lst1)) rests)))
  (cond ((= n 0) (cons nil nil))
        ((or (< n 0) (null? lst)) nil)
        ((< n (car lst)) (list-change n (cdr lst)))
        (else (append (cons-all (car lst)
                                (list-change (- n (car lst)) lst))
                      (list-change n (cdr lst)))))
)
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19

           (cons (list 'lambda
                 (let-to-lambda (car (zip values)))
                 (let-to-lambda (car body)))
                 (let-to-lambda (cadr (zip values))))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
