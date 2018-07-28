;; Extra Scheme Questions ;;


; Q5
(define lst
  'the_original_picture_damaged_so_could_not_finish
)

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (filter (lambda (x) (not (= x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

; Q8
(define (max a b) (if (> a b) a b))
(define (min a b) (if (> a b) b a))
(define (gcd a b)
  (if (or (= a 0) (= b 0))
      (max a b)

      (if (= (modulo (max a b) (min a b)) 0)
          (min a b)
          (gcd (- (max a b) (min a b)) (min a b))))

)

;;; Tests
(gcd 24 60)
; expect 12
(gcd 1071 462)
; expect 21

; Q9
(define (no-repeats s)
  (if (null? s)
      ()
      (cons (car s)
            (no-repeats (filter (lambda (x) (not (= x (car s))))
                                     (cdr s) ))))
)

; Q10
(define (substitute s old new)
  (if (null? s)
      ()
      (if (pair? (car s))
          (cons (substitute (car s) old new) (substitute (cdr s) old new))
          (if (eq? (car s) old)
              (cons new (substitute (cdr s) old new))
              (cons (car s) (substitute (cdr s) old new)))))
)

; Q11
(define (sub-all s olds news)
        (if (null? olds)
            s
            (sub-all (substitute s (car olds) (car news))
                    (cdr olds)
                    (cdr news)))
)
