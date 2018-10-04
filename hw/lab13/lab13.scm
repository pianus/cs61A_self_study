; Q1
(define (compose-all funcs)
  (define (helper funcs x)
      (if (null? funcs)
          x
          (helper (cdr funcs) ((car funcs) x) )))
  (define (composed x)
      (helper funcs x))
  composed
)

; Q2
(define (tail-replicate x n)
  (define (helper x lst n)
    (if (= n 0)
        lst
        (helper x (cons x lst) (- n 1))))
  (helper x nil n)
)
