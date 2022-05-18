;; use simpler ~/.emacs config file
(setq load-home-init-file t)

(global-set-key "\C-h" 'delete-backward-char)
(global-set-key "\C-x?" 'help-command)

;; map the mouse wheel
(global-set-key [button4] '(lambda() (interactive) (scroll-down 3)))
(global-set-key [button5] '(lambda() (interactive) (scroll-up 3)))



