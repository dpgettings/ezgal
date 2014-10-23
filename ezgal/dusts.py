import numpy as np
__ver__ = '1.0'

class dust_wrapper(object):
	""" dust_wrapper class.  EzGal wraps this class around the dust function.  It takes care of the 
	details of passing or not passing parameters """

	func = ''		# sfh function
	args = ()		# extra arguments to pass on call
	has_args = False	# whether or not there are actually any extra arguments

	def __init__( self, function, args ):

		self.func = function

		if type( args ) == type( () ) and len( args ) > 0:
			self.has_args = True
			self.args = args

	def __call__( self, time, ls ):

		if self.has_args:
			return self.func( time, ls, *self.args )
		else:
			return self.func( time, ls )

class charlot_fall(object):
	""" callable-object implementation of the Charlot and Fall (2000) dust law """
	tau1 = 0.0
	tau2 = 0.0
	tbreak = 0.0

	def __init__( self, tau1=1.0, tau2=0.5, tbreak=0.01 ):
		""" dust_obj = charlot_fall( tau1=1.0, tau2=0.3, tbreak=0.01 )
		Return a callable object for returning the dimming factor as a function of age
		for a Charlot and Fall (2000) dust law.  The dimming is:
		
		np.exp( -1*Tau(t)(lambda/5500angstroms) )
		
		Where Tau(t) = `tau1` for t < `tbreak` (in gyrs) and `tau2` otherwise. """

		self.tau1 = tau1
		self.tau2 = tau2
		self.tbreak = tbreak

	def __call__( self, ts, ls ):

		ls = np.asarray( ls )
		ts = np.asarray( ts )
		ls.shape = (ls.size,1)
		ts.shape = (1,ts.size)

		taus = np.asarray( [self.tau1]*ts.size )
		m = (ts > self.tbreak).ravel()
		if m.sum(): taus[m] = self.tau2

		return np.exp( -1.0*taus*(ls/5500.0)**-0.7 )