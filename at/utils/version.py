from logging import getLogger
from subprocess import run as proc_run, CalledProcessError

from weasyprint import __version__ as weasyprint_version
from xml2rfc import __version__ as xml2rfc_version


def get_kramdown_rfc2629_version(logger=getLogger()):
    '''Return kramdown-rfc2629 version'''

    output = proc_run(
                args=['kramdown-rfc2629', '--version'],
                capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').replace(
                'kramdown-rfc2629', '').strip()
    except CalledProcessError:
        logger.info('kramdown-rfc2629 error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_mmark_version(logger=getLogger()):
    '''Return mmark version'''

    output = proc_run(args=['mmark', '--version'], capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').strip()
    except CalledProcessError:
        logger.info('mmark error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_id2xml_version(logger=getLogger()):
    '''Return id2xml version'''

    output = proc_run(args=['id2xml', '--version'], capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').replace('id2xml', '').strip()
    except CalledProcessError:
        logger.info('id2xml error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_xml2rfc_version():
    '''Return xml2rfc version'''

    return xml2rfc_version


def get_weasyprint_version():
    '''Return Weasyprint version'''

    return weasyprint_version


def get_goat_version(logger=getLogger()):
    '''Return goat version'''

    output = proc_run(args=['goat', '--version'], capture_output=True)

    try:
        output.check_returncode()
        version = output.stdout.decode('utf-8').strip()
        if not version:
            return output.stderr.decode('utf-8').strip()
    except CalledProcessError:
        logger.info('goat error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_idnits_version(logger=getLogger()):
    '''Return idnits version'''

    output = proc_run(args=['idnits', '--version'], capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').replace('idnits', '').strip()
    except CalledProcessError:
        logger.info('idnits error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_aasvg_version(logger=getLogger()):
    '''Return aasvg version'''

    output = proc_run(args=['aasvg', '--version'], capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').replace('aasvg', '').strip()
    except CalledProcessError:
        logger.info('aasvg error: {}'.format(
            output.stderr.decode('utf-8')))
        return None


def get_iddiff_version(logger=getLogger()):
    '''Return iddiff version'''

    output = proc_run(args=['iddiff', '--version'], capture_output=True)

    try:
        output.check_returncode()
        return output.stdout.decode('utf-8').replace('iddiff', '').strip()
    except CalledProcessError:
        logger.info('iddiff error: {}'.format(
            output.stderr.decode('utf-8')))
        return None
