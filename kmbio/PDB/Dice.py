# Copyright (C) 2002, Thomas Hamelryck (thamelry@binf.ku.dk)
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.

import re
import logging

from kmbio.PDB.PDBIO import PDBIO

logger = logging.getLogger(__name__)

_hydrogen = re.compile("[123 ]*H.*")


class ChainSelector(object):
    """
    Only accepts residues with right chainid
    and between start and end. Remove hydrogens, waters and ligands.
    Only use model 0 by default.
    """
    def __init__(self, chain_id, start, end, model_id=0):
        self.chain_id = chain_id
        self.start = start
        self.end = end
        self.model_id = model_id

    def accept_model(self, model):
        # model - only keep model 0
        if model.id == self.model_id:
            return 1
        return 0

    def accept_chain(self, chain):
        if chain.id == self.chain_id:
            return 1
        return 0

    def accept_residue(self, residue):
        # residue - between start and end
        hetatm_flag, resseq, icode = residue.id
        if hetatm_flag != " ":
            # skip HETATMS
            return 0
        if icode != " ":
            logger.warning("WARNING: Icode at %s", residue.id)
        if self.start <= resseq <= self.end:
            return 1
        return 0

    def accept_atom(self, atom):
        # atoms - get rid of hydrogens
        name = atom.id
        if _hydrogen.match(name):
            return 0
        else:
            return 1


def extract(structure, chain_id, start, end, filename):
    """
    Write out selected portion to filename.
    """
    sel = ChainSelector(chain_id, start, end)
    io = PDBIO()
    io.set_structure(structure)
    io.save(filename, sel)


if __name__ == "__main__":

    from kmbio.PDB.PDBParser import PDBParser

    import sys

    p = PDBParser()
    s = p.get_structure("scr", sys.argv[1])

    extract(s, " ", 1, 100, "out.pdb")