import unittest
import os
import subprocess


class TestAssembly(unittest.TestCase):
    '''
        Test the assembly workflows: assembly_workflow_metaspades, assembly_workflow_megahit, assembly_workflow_all
        We test by checking if the correct files are created at the end of the workflow.
    '''
    
    def setUp(self):
        os.chdir("../workflows/")
        os.environ['SINGULARITY_BINDPATH'] = "data:/tmp"
     
    '''
    def test_1_assembly_metaspades_workflow(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_metaspades_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.metaspades.contigs.fa")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.metaspades.contigs.fa")
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2))  
             
    def test_2_assembly_megahit_workflow(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_megahit_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.megahit.contigs.fa")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.megahit.contigs.fa")
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2))    
        
    def test_3_assembly_workflow_all(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_all_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.megahit.contigs.fa")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.megahit.contigs.fa")
        filename_3 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.metaspades.contigs.fa")
        filename_4 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.megahit.contigs.fa") 
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2) and os.path.isfile(filename_3) and os.path.isfile(filename_4) )  
     
    def test_4_assembly_spades_workflow(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_spades_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30_k21_33_55.spades.contigs.fa")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2_k21_33_55.spades.contigs.fa")
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2)) 
        
    def test_5_assembly_plasmidspades_workflow(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_plasmidspades_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.plasmidspades.contigs.fa")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.plasmidspades.contigs.fa")
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2)) 
        
             
    def test_6_assembly_quast_workflow(self): 
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_quast_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.megahit_quast/report.tsv")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.megahit_quast/report.tsv")
        filename_3 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.metaspades_quast/report.tsv")
        filename_4 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.metaspades_quast/report.tsv")
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2) and os.path.isfile(filename_3) and os.path.isfile(filename_4) )
    '''

    #terminal
    def test_7_assembly_multiqc_workflow(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_multiqc_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads.megahit_multiqc_report_data/multiqc.log")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads.metaspades_multiqc_report_data/multiqc.log")        
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2))
            
    #terminal
    def test_8_assembly_metaquast_workflow(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_metaquast_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.megahit_metaquast")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.megahit_metaquast")        
        filename_3 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.metaspades_metaquast")
        filename_4 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.metaspades_metaquast")
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2) and os.path.isfile(filename_3) and os.path.isfile(filename_4))
    
    #terminal
    def test_9_assembly_quast_reference_with_spades_workflow(self):
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_quast_reference_with_spades_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.spades_quast")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.spades_quast")        
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2))
        
    #terminal
    def test_10_assembly_quast_reference_with_plasmidspades_workflow(self):        
        snakemake_command = "snakemake -q --cores --use-singularity --configfile=../test/test_assembly_workflow.json assembly_quast_reference_with_plasmidspades_workflow"
        subprocess.run([snakemake_command], shell=True)
        dirname = os.getcwd()
        filename_1 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim30.plasmidspades-quast")
        filename_2 = os.path.join(dirname, "data/SRR606249_subset10_1_reads_trim2.plasmidspades-quast")        
        self.assertTrue(os.path.isfile(filename_1) and os.path.isfile(filename_2))
        
        
if __name__ == '__main__':
    unittest.main()        
 
