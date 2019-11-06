# /home/maciek/odoo-dev/gal/galicea/gal_jpk/schemas/generated/http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_02_05_eD_ORDZU_/bindings.py
# -*- coding: utf-8 -*-
# @generated
# PyXB bindings for NM:4a041b7b29bcbc66ba97a8250d44081500838da3
# Generated 2018-03-08 13:30:04.721339 by PyXB version 1.2.5 using Python 2.7.12.final.0
# Namespace http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ [xmlns:zzu]

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6998c690-22cc-11e8-9d15-8c705ac2b4bc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
from ..http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy_ import bindings as _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.byte, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 20, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON._CF_enumeration.addEnumeration(unicode_value='3', tag=None)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}TKodFormularza_ZU
class TKodFormularza_ZU (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Symbol wzoru formularza"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TKodFormularza_ZU')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 28, 1)
    _Documentation = 'Symbol wzoru formularza'
TKodFormularza_ZU._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=TKodFormularza_ZU, enum_prefix=None)
TKodFormularza_ZU.ORD_ZU = TKodFormularza_ZU._CF_enumeration.addEnumeration(unicode_value='ORD-ZU', tag='ORD_ZU')
TKodFormularza_ZU._InitializeFacetMap(TKodFormularza_ZU._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TKodFormularza_ZU', TKodFormularza_ZU)
_module_typeBindings.TKodFormularza_ZU = TKodFormularza_ZU

# Complex type {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}TNaglowek_ORD-ZU with content type ELEMENT_ONLY
class TNaglowek_ORD_ZU (pyxb.binding.basis.complexTypeDefinition):
    """Nagłówek deklaracji"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TNaglowek_ORD-ZU')
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 4, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}KodFormularza uses Python identifier KodFormularza
    __KodFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), 'KodFormularza', '__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZU_TNaglowek_ORD_ZU_httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZUKodFormularza', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 9, 3), )

    
    KodFormularza = property(__KodFormularza.value, __KodFormularza.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}WariantFormularza uses Python identifier WariantFormularza
    __WariantFormularza = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), 'WariantFormularza', '__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZU_TNaglowek_ORD_ZU_httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZUWariantFormularza', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 19, 3), )

    
    WariantFormularza = property(__WariantFormularza.value, __WariantFormularza.set, None, None)

    _ElementMap.update({
        __KodFormularza.name() : __KodFormularza,
        __WariantFormularza.name() : __WariantFormularza
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TNaglowek_ORD_ZU = TNaglowek_ORD_ZU
Namespace.addCategoryObject('typeBinding', 'TNaglowek_ORD-ZU', TNaglowek_ORD_ZU)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 40, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}Naglowek uses Python identifier Naglowek
    __Naglowek = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), 'Naglowek', '__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZU_CTD_ANON_httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZUNaglowek', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 42, 4), )

    
    Naglowek = property(__Naglowek.value, __Naglowek.set, None, None)

    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}PozycjeSzczegolowe uses Python identifier PozycjeSzczegolowe
    __PozycjeSzczegolowe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe'), 'PozycjeSzczegolowe', '__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZU_CTD_ANON_httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZUPozycjeSzczegolowe', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 43, 4), )

    
    PozycjeSzczegolowe = property(__PozycjeSzczegolowe.value, __PozycjeSzczegolowe.set, None, None)

    _ElementMap.update({
        __Naglowek.name() : __Naglowek,
        __PozycjeSzczegolowe.name() : __PozycjeSzczegolowe
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 44, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/}P_13 uses Python identifier P_13
    __P_13 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'P_13'), 'P_13', '__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZU_CTD_ANON__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZUP_13', False, pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 46, 7), )

    
    P_13 = property(__P_13.value, __P_13.set, None, 'Tre\u015b\u0107 uzasadnienia')

    _ElementMap.update({
        __P_13.name() : __P_13
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = TKodFormularza_ZU
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 10, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is TKodFormularza_ZU
    
    # Attribute kodSystemowy uses Python identifier kodSystemowy
    __kodSystemowy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'kodSystemowy'), 'kodSystemowy', '__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZU_CTD_ANON_2_kodSystemowy', pyxb.binding.datatypes.string, fixed=True, unicode_default='ORD-ZU (3)', required=True)
    __kodSystemowy._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 13, 7)
    __kodSystemowy._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 13, 7)
    
    kodSystemowy = property(__kodSystemowy.value, __kodSystemowy.set, None, None)

    
    # Attribute wersjaSchemy uses Python identifier wersjaSchemy
    __wersjaSchemy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'wersjaSchemy'), 'wersjaSchemy', '__httpcrd_gov_plxmlschematydziedzinowemf20160205eDORDZU_CTD_ANON_2_wersjaSchemy', pyxb.binding.datatypes.string, fixed=True, unicode_default='1-0E', required=True)
    __wersjaSchemy._DeclarationLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 14, 7)
    __wersjaSchemy._UseLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 14, 7)
    
    wersjaSchemy = property(__wersjaSchemy.value, __wersjaSchemy.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __kodSystemowy.name() : __kodSystemowy,
        __wersjaSchemy.name() : __wersjaSchemy
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Treść uzasadnienia"""
    _TypeDefinition = _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TTekstowy
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 50, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is _ImportedBinding_generated_http___crd_gov_pl_xml_schematy_dziedzinowe_mf_2016_01_25_eD_DefinicjeTypy__bindings.TTekstowy
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


Zalacznik_ORD_ZU = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Zalacznik_ORD-ZU'), CTD_ANON, documentation='UZASADNIENIE PRZYCZYN KOREKTY DEKLARACJI', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 36, 1))
Namespace.addCategoryObject('elementBinding', Zalacznik_ORD_ZU.name().localName(), Zalacznik_ORD_ZU)



TNaglowek_ORD_ZU._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza'), CTD_ANON_2, scope=TNaglowek_ORD_ZU, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 9, 3)))

TNaglowek_ORD_ZU._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza'), STD_ANON, scope=TNaglowek_ORD_ZU, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 19, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TNaglowek_ORD_ZU._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KodFormularza')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 9, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TNaglowek_ORD_ZU._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WariantFormularza')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 19, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TNaglowek_ORD_ZU._Automaton = _BuildAutomaton()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Naglowek'), TNaglowek_ORD_ZU, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 42, 4)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe'), CTD_ANON_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 43, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Naglowek')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 42, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PozycjeSzczegolowe')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 43, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'P_13'), CTD_ANON_3, scope=CTD_ANON_, documentation='Tre\u015b\u0107 uzasadnienia', location=pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 46, 7)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'P_13')), pyxb.utils.utility.Location('http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2016/02/05/eD/ORDZU/ORD-ZU(3)_v1-0E.xsd', 46, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_2()

