
def list_to_dictionary(l, keys=None):
  """

		:param l:
		:param keys:
		:return:
		"""
  D = {key: item for item, key in zip(l, keys)}
  return D

def list_of_list_to_dictionary(l, keys=None):
  if not keys:
    Func = lambda subli: list_to_dictionary(subli, l[0])
    l = [Func(i) for i in l[1:]]
    else:
      Func = lambda subli:list_to_dictionary(subli, keys)
      l = [Func(i) for i in l]
      return l