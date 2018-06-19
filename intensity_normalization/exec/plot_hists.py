#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
intensity_normalization.exec.plot_hists

plot the histograms over one another

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: May 21, 2018
"""

import argparse
import logging
import sys
import warnings

import matplotlib.pyplot as plt

with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=FutureWarning)
    from intensity_normalization.plot.hist import all_hists


def arg_parser():
    parser = argparse.ArgumentParser(description='Plot all histograms for a set of nifti MR images')
    parser.add_argument('-i', '--img-dir', type=str, required=True,
                        help='path to directory with images to be processed '
                             '(should all be T1w contrast)')
    parser.add_argument('-m', '--mask-dir', type=str, default=None,
                        help='directory to brain masks for imgs')
    parser.add_argument('-t', '--plot-title', type=str, default=None,
                        help='title for output histogram plot')
    parser.add_argument('-o', '--out-name', type=str, default='hist.png',
                        help='name for output histogram (default: hist.png)')
    parser.add_argument('-a', '--alpha', type=float, default=0.8,
                        help='alpha parameter for line plots')
    parser.add_argument('-f', '--figsize', type=tuple, default=(12,10),
                        help='alpha parameter for line plots')
    parser.add_argument('-l', '--linewidth', type=float, default=3,
                        help='linewidth parameter for line plots')
    parser.add_argument('-v', '--verbosity', action="count", default=0,
                        help="increase output verbosity (e.g., -vv is more than -v)")
    return parser


def main():
    args = arg_parser().parse_args()
    if args.verbosity == 1:
        level = logging.getLevelName('INFO')
    elif args.verbosity >= 2:
        level = logging.getLevelName('DEBUG')
    else:
        level = logging.getLevelName('WARNING')
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=level)
    logger = logging.getLogger(__name__)
    try:
        ax = all_hists(args.img_dir, args.mask_dir, alpha=args.alpha, figsize=args.figsize, lw=args.linewidth)
        if args.plot_title is not None:
            ax.set_title(args.plot_title)
        plt.savefig(args.out_name)
        return 0
    except Exception as e:
        logger.exception(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())