# Certora Verification — credit_rail
# Usage:
#   make interest-math    # fastest, start here
#   make credit-policy
#   make loan-engine
#   make tranche-pool
#   make all              # run all specs

.PHONY: all interest-math credit-policy loan-engine tranche-pool

all: interest-math credit-policy loan-engine tranche-pool

interest-math:
	cd .. && certoraRun certora/confs/InterestMath.conf

credit-policy:
	cd .. && certoraRun certora/confs/CreditPolicy.conf

loan-engine:
	cd .. && certoraRun certora/confs/LoanEngine.conf

tranche-pool:
	cd .. && certoraRun certora/confs/TranchePool.conf
